"""
Created on 2016/7/28
@author: lijc210@163.com
Desc: 功能描述。
pip install hdfs
"""
from hdfs.client import InsecureClient


class HdfsClient:
    def __init__(self, host="", user=""):
        self.client = InsecureClient(host, user=user)

    def list(self, hdfs_path):
        """
        返回目录下的文件
        :param hdfs_path:
        :return:
        """
        return self.client.list(hdfs_path, status=False)

    def read(self, hdfs_path=""):
        """
        返回文本内容
        :param hdfs_path:
        :return:
        """
        with self.client.read(hdfs_path, encoding="utf-8", delimiter="\n") as fs:
            yield from fs

    def write(self, hdfs_path="", data=""):
        """
        写入
        :param hdfs_path:
        :param local_path:
        :return:
        """
        with self.client.write(
            hdfs_path, data, encoding="utf-8", overwrite=False
        ) as writer:
            writer.write(data)

    def download(self, hdfs_path="", local_path="", overwrite=False):
        download_path = self.client.download(hdfs_path, local_path, overwrite=overwrite)
        return download_path

    def upload(self, hdfs_path="", local_path=""):
        """
        上传
        :param hdfs_path:
        :param local_path:
        :return:
        """
        upload_path = self.client.upload(hdfs_path, local_path, overwrite=True)
        return upload_path


if __name__ == "__main__":
    ##### 连接
    hdfs_client = HdfsClient(host="http://10.10.23.11:50070", user="hadoop")

    ##### list
    path = "/user/qizhiusera/warehouse/tmp/tmp_lijc_test"
    print(hdfs_client.list(path))

    ##### read
    path = "/user/qizhiusera/warehouse/tmp/tmp_lijc_test/test.txt"
    fs = hdfs_client.read(path)
    with open("test.txt", "w") as f:
        for line in fs:
            print(line)
            f.write(line + "\n")

    ##### write
    path = "/user/qizhiusera/warehouse/tmp/tmp_lijc_test/test.txt"
    text = "a" + "\t" + "b"
    hdfs_client.write(hdfs_path=path, data=text)

    #### download
    hdfs_client.download(
        hdfs_path="/user/qizhiusera/warehouse/tmp/tmp_lijc_test/test.txt",
        local_path="test.txt",
        overwrite=True,
    )

    ### upload
    hdfs_path = "/user/qizhiusera/warehouse/tmp/tmp_lijc_test"
    local_path = "test.txt"
    hdfs_client.upload(hdfs_path, local_path)
