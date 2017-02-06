# This file is subject to the terms and conditions defined in file 'LICENSE',
# which is part of this repository.


def test_environment_file_exists(File):
    file = File("/etc/environment")
    assert file.exists
    assert file.is_file


def test_apt_proxy_file_exists(File, SystemInfo):
    if SystemInfo.distribution == 'ubuntu':
        file = File("/etc/apt/apt.conf.d/01proxy")
        assert file.exists
        assert file.is_file
    elif SystemInfo.distribution == 'centos':
        assert True
