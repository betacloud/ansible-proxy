def test_environment_file(host):
    f = host.file("/etc/environment")
    assert f.exists
    assert f.is_file
