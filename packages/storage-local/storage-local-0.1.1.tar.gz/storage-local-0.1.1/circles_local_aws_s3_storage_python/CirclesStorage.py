from circles_local_aws_s3_storage_python.FileTypeDB import file_type_db
import os
from circles_local_aws_s3_storage_python.AWSStorage import AwsS3Storage
from dotenv.main import load_dotenv
load_dotenv()
import re
from logger_local.LoggerService import LoggerService

class circles_storage:

    def __init__(self,test=False):
        self.s3 = AwsS3Storage(os.getenv("BUCKET_NAME"), os.getenv("REGION"))
        self.db = file_type_db()
        self.test=test
        self.lgrins=LoggerService()
        self.lgrins.init({'component_id':"13"})
        self.system_check()

    # returns the folder name from DB according to entity_type_id
    def _get_folder(self, entity_type_id):
        select_stmt = "SELECT file_type FROM storage.file_type_table WHERE id = %s"
        select_data = (entity_type_id)
        return self.db.select_from_DB(select_stmt, select_data)

    def _get_region_and_folder(self, profile_id, entity_type_id):
        folder = self._get_folder(entity_type_id)
        region = os.getenv("REGION")
        return [folder, region]

    #
    def put(self, profile_id, entity_type_id, file_name, local_file_path):
        """uploads a file from local computer to S3 and return ID of the file in the storage DB

        Args:
            profile_id int: user ID
            entity_type_id int: type of the file - 
                                1 - Profile Image
                                2 - Coverage Image
                                3 - Personal Introduction Video
                                4 - Scanned Diving Licesnse 
                                5 - Scanned Passport
            file_name string: file name including extention, i.e test.txt
            local_file_path string: path to file location, i.e path/to/file/
        Returns:
            int: ID of the file in the storage DB
        """
        folder_and_region = self._get_region_and_folder(
            profile_id, entity_type_id)
        file_database_id = self.s3.upload_file(local_file_path, file_name,
                                               folder_and_region[0]+'/', profile_id)
        return file_database_id


    def preserve_letters(self,input_string):
        """Preserves only letters and spaces in a given string

        Args:
            input_string string: unmodified string
        """
        # Use a regular expression to match only letters (A-Z and a-z)
        pattern = r"[^a-zA-Z\s]"
        preserved_string = re.sub(pattern, "", input_string)
        return preserved_string


    def download_by_storage_id(self, storage_id):
        """Downlaods file from S3 to local computer using only storage id

        Args:
            storage_id int: Row number to get information from storage_table
        """
        select_stmt = "SELECT created_user_id, path, filename FROM storage.storage_table WHERE id = %s"
        select_data = (storage_id)
        self.db.cursor.execute(select_stmt, [select_data])
        profile_id, folder, file_name = self.db.cursor.fetchall()[0]
        path_local = os.path.join(os.getcwd(), file_name)
        self.s3.download_file(folder+file_name,path_local)
        return path_local
        
    def system_check(self):
        """Checking for Credentials-based errors"""
        self.lgrins.start()
        if os.getenv("BUCKET_NAME") is None or self.test is True:
           self.lgrins.critical("BUCKET_NAME not specified in .env, please add")
        if os.getenv("REGION") is None or self.test is True:
           self.lgrins.critical("REGION not specified in .env, please add")
        try:
           cursor =  self.db.cursor
        except:
           self.lgrings.critical("Unable to create cursor")

        try:
           if self.test is True:
              raise ValueError("Testing logger")
           sql_query = f"DESCRIBE logger.logger_table"
           cursor.execute(sql_query)
           columns_info = cursor.fetchall()
           print(columns_info)
        except:
           self.lgrins.critical("Unable to access logger.logger_table. Try confirming if user has access")

        try:
           if self.test is True:
              raise ValueError("Testing logger")
           sql_query = f"DESCRIBE storage.storage_table"
           cursor.execute(sql_query)
           columns_info = cursor.fetchall()
           print(columns_info)
        except:
           self.lgrins.critical("Unable to access storage.storage_table. Try confirming if user has access")
        self.lgrins.end()

    def download(self, profile_id, entity_type_id, file_name, local_path):
        """Downlaods file from S3 to local computer

        Args:
            entity_type_id int: 1 - Profile Image
                                2 - Coverage Image
                                3 - Personal Introduction Video
                                4 - Scanned Diving Licesnse 
                                5 - Scanned Passport
            file_name string: file name include extention, i.e test.txt
            local_path string: where to save the file, include file extention,
            i.e path/to/file/downloaded_test.txt
        """
        folder_and_region = self._get_region_and_folder(
            profile_id, entity_type_id)
        remote_file_path = folder_and_region[0]+'/'+file_name
        self.s3.download_file(remote_file_path, local_path)
