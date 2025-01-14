import platform
import requests
import sys

from slumber.serialize import Serializer
from slumber.exceptions import HttpClientError, HttpServerError

from .clientAPI import clientAPI
from . import exceptions 
from ._version import __version__

class client (object):

    user_agent = 'scw-sdk/%s Python/%s %s' % (__version__, ' '.join(sys.version.split()), platform.platform())

    def __init__ (self, host:str=None, token:str=None, user_agent:str=None, usermail:str=None, passwd:str=None):

        import os

        if host == None:
            if 'TCP_HOST' in os.environ.keys ():
                host = os.environ['TCP_HOST']
            else:
                host = "https://api.thecrossproduct.xyz/v1"

        self.host = host

        if user_agent:
            self.user_agent = user_agent

        self.token = None

        if token:
            self.token = token

        elif usermail and passwd:

            from requests.auth import HTTPBasicAuth
            import json
            from .logs import warning

            resp = clientAPI (self.host, 
                              self.host,
                              session=self._make_requests_session(),
                              auth=HTTPBasicAuth(usermail,passwd),
                           ).auth.login.get()

            self.token = resp['token']

        if not self.token:
            if 'TCP_API_TOKEN' not in os.environ.keys():
                raise exceptions.InvalidCredentials ("No token available: either use BasicAuth or set the env var $TCP_API_TOKEN") 

            self.token = os.environ['TCP_API_TOKEN']

    def _make_requests_session (self):

        session = requests.Session ()

        session.headers.update({'User-Agent': self.user_agent})

        if self.token:

            session.headers.update ({'Authorization': f'Bearer {self.token}'})

        return session

    def query (self, **kwargs):

        api = clientAPI (self.host,
                         self.host,
                         session=self._make_requests_session(),
                         serializer=Serializer(default="json"),
                         **kwargs)

        return api

    def _get_endpoints (self):

        api = clientAPI (self.host,
                         self.host + '/help',
                         session=self._make_requests_session(),
                         serializer=Serializer(default="json"))

        return api._get_resource(**api._store).get()

    def help (self):

        import textwrap

        resp = self._get_endpoints ()

        lines = []
        for endpoint in resp:
            lines.append ([" OR ".join(endpoint['methods']), 'query()'+endpoint["endpoint"].replace('/', '.')])

        max_first = max([len(x[0]) for x in lines])

        print ("Python SDK to query TCP's API.\n"
               "\n"
               "You can connect to your TCP account by either setting the environment variable TCP_API_TOKEN\n"
               "Alternatively, you can connect using the following code:\n"
               "\n"
               "import tcp\n"
               "client = tcp.client (usermail=\"user@mail.co\", passwd=\"passwd\")\n"
               "\n"
               "If you're looking to send a GET HTTP request against our API, like:\n"
               "\n"
               " GET https://{hostname}/{vX}/auth\n"
               "\n"
               "You only need to call the following pythonic code:\n"
               "\n"
               "import tcp\n"
               "client = tcp.client ()\n"
               "client.query().auth.get()\n"
               "\n"
               "The query method returns a slumber.API object.\n"
               "The latter handles all the excruciating details of the requests.\n"
               "\n"
              )

        print ("The following endpoints are available:\n")

        for line in lines:
            print ('{0:<30}\t{1:<}'.format(line[0], line[1]))

        print ("\n\nOther methods includes:\n"
               "\n"
               "help\t\t- this message\n"
               "download\t- from TCP S3 storage to your local storage\n"
               "upload\t\t- from your local storage to TCP S3 storage\n"
               "dashboard\t- interactive overview of your account ressources")

    def upload (self, src_local:str, dest_s3:str, max_part_size:str=None):
        '''
        Multipart upload of a file from local repository to S3 repository.

        Args:
            src_local (str): path to your file on your local computer
            dest_s3 (str): desired path in TCP S3 bucket
            max_part_size (str): optional. Size of each part to be sent. Either an int (number of bytes) or a human formatted string (example: "10Gb") 

        Exceptions:
            tcp.exceptions.tcpUploadException

        Notes:

            Works accordingly to the following sequence:
                1. Defining the target space in the S3 repository.
                2. Partionning the file and sending each part to the target space
                3. Merging files and completing the upload

            Internally it uses the following TCP endpoints:
                - POST generate_presigned_multipart_post 
                - POST complete_multipart_post
        '''
        import os

        # Uploading directory
        if os.path.isdir (src_local):
            root_in_s3 = os.path.basename (src_local)

            for root, dirs, files in os.walk (src_local):
                for file in files:
                    self.upload (os.path.join(root,file), 
                                 os.path.join(
                                     os.path.join(dest_s3,root_in_s3), 
                                     os.path.join(root[len(src_local):],file)
                                     ),
                                 max_part_size
                                 )
            return

        #TODO adding multithread and retry process when error
        #1: S3 target space definition
        file_size = str(os.path.getsize(src_local))
        presigned_body={"uri": dest_s3,"size": file_size}

        if max_part_size:
            presigned_body.update({"part_size":max_part_size})
        
        try:
            resp=self.query().data.generate_presigned_multipart_post.post(presigned_body)
        except slumber.exceptions.SlumberHttpBaseException as err:
            raise exceptions.UploadException (str(err), err.__dict__)

        #2: File's parts loading
        uploadId=resp["upload_id"]
        urls=resp["parts"]
        part_size = resp["part_size"]
        completed_parts=[]

        has_failed = False

        with open(src_local, 'rb') as f:
            for part_no,url in enumerate(urls):
                file_data = f.read(int(part_size))
           
                resp=requests.put(url, data=file_data)

                if resp.status_code != 200:
                    has_failed = True
                    break
                                
                completed_parts.append({'ETag': resp.headers['ETag'].replace('"',''), 'PartNumber': part_no+1})

        body = {}

        # A part has failed, we abort.
        if has_failed:
            body['upload_id'] = uploadId
            body['uri'] = dest_s3
            self.query().data.abort_multipart_post.post (body)

            number_of_parts_done = len(completed_parts)
            total_number_of_parts = len(urls)

            raise exceptions.UploadError (f"Part number {number_of_parts_done} failed ({total_number_of_parts} in totals). The multi-part upload was aborted")

        #3: Parts concatenation and end of upload
        body["upload_id"] = uploadId
        body["parts"] = completed_parts
        body["uri"] = dest_s3

        try:
            self.query().data.complete_multipart_post.post(body)
        except slumber.exceptions.SlumberHttpBaseException as err:
            raise exceptions.UploadException (str(err), err.__dict__)

    def download (self, src_s3, dest_local, chunk_size=8192):
        '''
        Download of a file from local repository to S3 repository.

        Args:
            src_s3 (str): path in TCP S3 bucket 
            dest_local (str): desired path in your local computer 
            chunk_size (int): desired chunk size for streaming download

        Exceptions:
            tcp.exceptions.tcpDownloadException

        Notes:

            Works accordingly to the following sequence:
                1. Get a temporary link to our S3 
                2. Download file from that link using a stream 

            Internally it uses the following TCP endpoints:
                - POST generate_presigned_get
        '''

        body = {} 
        body['uri'] = src_s3

        try:
            resp = self.query ().data.generate_presigned_get.post (body)
        except slumber.exceptions.SlumberHttpBaseException as err:
            raise exceptions.DownloadException (str(err), err.__dict__)

        url = resp['url']

        try: 
            with requests.get(url, stream=True) as r:
                r.raise_for_status ()
                with open (dest_local, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=chunk_size):
                        f.write (chunk)
        except requests.exceptions.HTTPError as err:
            raise exceptions.DownloadException (str(err), err.__dict__)

    def dashboard (self, refresh_delay=5):
        '''
        Print an overview of all processes.

        Args:
            refresh_delay (int): refresh every X seconds
        '''

        from .dashboard import dashboard
        dashboard (self, refresh_delay)

