# pip install paramiko tqdm
from paramiko import Transport, SFTPClient
import logging
import os
from time import sleep
from tqdm import tqdm

class LittleSFTPCode:

    def __init__(self, host, username, password):
        try: 
            logging.basicConfig(format='%(levelname)s - %(message)s', level=logging.INFO)

            transport = Transport(sock=(host))
            transport.connect(username=username, password=password)
            self.connection = SFTPClient.from_transport(transport)
        except:
             logging.error('Can not able to conenct to server')
    def __del__(self):
        #logging.info('closing connection', self.connection) 
        try: 
            self.connection.close()
        except:
             logging.error('connection error')
    
    def uploading_info(self, uploaded_file_size, total_file_size):
        logging.info('uploaded_file_size : {} total_file_size : {}'.format(uploaded_file_size, total_file_size))

    def rm_recursive(self, dest):
        files = self.connection.listdir(dest)
        files_tqdm =tqdm(files, ascii=True ,desc='deleting files', ncols=100) 
        for f in files_tqdm:
            filepath = os.path.join(dest, f)
            try:
                files_tqdm.set_description(f'deleting {f}')
                self.connection.remove(filepath)
                #logging.info(f'{f} deleted successfully')
                sleep(0.01)
            except IOError:
                self.rm_recursive(filepath)

    def put_recursive(self, src, dest):
        files = os.listdir(src)
        files_tqdm = tqdm(files, ascii=True ,desc='uploading files', ncols=100)
        for f in files_tqdm:
            filepath_src = os.path.join(src, f)
            filepath_dest = os.path.join(dest, f)
            try:
                files_tqdm.set_description(f'uploading {f}')
                self.connection.put(localpath=filepath_src,
                remotepath=filepath_dest,
                callback = None,
                confirm = True
                )
                sleep(0.01)
            except IOError:
                self.put_recursive(filepath_src, filepath_dest)

    def put_single_file(self, src, dest):
        self.connection.put(localpath = src,
                remotepath= dest,
                callback = None,
                confirm = True
                )
        logging.info(f'{dest} uploaded successfully')
if __name__ == '__main__':


    def a_function():
        
        l = LittleSFTPCode('server.ip', 'username', 'password')

        l.rm_recursive('/home/deploy/bayview/repo/admin-app/build/')

        l.put_recursive('/Users/ujwal/Documents/admin-app/build/',
                        '/home/deploy/bayview/repo/admin-app/build/')

        l.put_single_file('/Users/ujwal/Documents/admin-app/version.txt',
                         '/home/deploy/bayview/repo/admin-app/version.txt')

    a_function()
