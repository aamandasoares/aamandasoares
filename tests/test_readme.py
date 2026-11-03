from pathlib import Path


README = Path(__file__).resolve().parents[1] / "README.md"


def test_readme_contem_secoes_e_links_do_portfolio() -> None:
    conteudo = README.read_text(encoding="utf-8")

    assert "# Olá, eu sou a Amanda Soares" in conteudo
    assert "## Projetos em destaque" in conteudo
    assert "## Em andamento" in conteudo
    assert "## Habilidades" in conteudo
    assert "## Contato" in conteudo
    assert "https://github.com/aamandasoares/assistente-rag-restaurante" in conteudo
    assert "https://github.com/aamandasoares/agente-pedidos" in conteudo
    assert "https://github.com/aamandasoares/Banco_de_dados_Triagem_hospitalar" in conteudo
    assert "https://carlosferreiraadvogado.com/" in conteudo