import os, uuid
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

#tts가 로컬에 저장이 되면, 그 파일 주소로 접근해서 azure storage에 업로드 하고 url 받으면 베스트
load_dotenv()
connect_str = os.environ.get('AZURE_STORAGE_CONNECTION_STRING')
container_name = "tts-files"
upload_file_path = "crawling/services/audio1.wav"
#업로드된 애 url 은
#https://newsttsstorage.blob.core.windows.net/tts-files/{blob_file_name}

def upload_tts(file_path: str, blob_file_name: str) -> str:
    try:
        # Quickstart code goes here
        account_url = "https://newsttsstorage.blob.core.windows.net"
        # Create the BlobServiceClient object
        blob_service_client = BlobServiceClient.from_connection_string(connect_str) 
        # Create a blob client using the local file name as the name for the blob
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_file_name)
        print("\nUploading to Azure Storage as blob:\n\t" + upload_file_path)
        # Upload the created file
        with open(file=upload_file_path, mode="rb") as data:
            blob_client.upload_blob(data)
            return f"https://newsttsstorage.blob.core.windows.net/tts-files/{blob_file_name}"
    except Exception as ex:
        print('Exception:')
        print(ex)
        return ""
    
if __name__ == "__main__":
    upload_tts('crawling/services/audio1.wav', "audio1.wav")