from getnet import Environment


def test_base_url():
    assert "https://api-sandbox.getnet.com.br" == Environment.SANDBOX.base_url()
    assert "https://api-homologacao.getnet.com.br" == Environment.HOMOLOG.base_url()
    assert "https://api.getnet.com.br" == Environment.PRODUCTION.base_url()
