# TXT Compiler

## 📝 Sobre o Projeto

Este projeto nasceu de uma necessidade pessoal de organização. Como profissional que participa de diversas reuniões, desenvolvi o hábito de fazer anotações rápidas no Bloco de Notas durante as reuniões, salvando-as diretamente na área de trabalho. Com o tempo, isso resultou em uma grande quantidade de arquivos .txt espalhados pela área de trabalho, tornando-a desorganizada e difícil de gerenciar.

## 🎯 Objetivo

O TXT Compiler foi criado para resolver este problema, oferecendo uma solução que:
- Compila todos os arquivos .txt em um único arquivo organizado
- Mantém um registro da data de última modificação de cada arquivo
- Move os arquivos originais para uma pasta de backup
- Mantém a área de trabalho limpa e organizada

## 💡 Motivação

A ideia surgiu durante a leitura do livro "Python Fluente" do autor Luciano Ramalho, que enfatiza a importância de escrever código Python seguindo as melhores práticas e convenções da linguagem. Inspirado pelos conceitos apresentados no livro, decidi aplicar estes princípios neste projeto, incluindo:

- Type hints
- Docstrings detalhadas
- Uso de `pathlib` para manipulação de caminhos
- Funções pequenas e específicas
- Código limpo e legível
- Tratamento adequado de exceções

## 🛠️ Funcionalidades

- Compilação automática de arquivos .txt
- Ordenação por data de modificação
- Criação de cabeçalhos com informações de data
- Backup automático dos arquivos originais
- Tratamento de erros robusto

## 📚 Aprendizados

Este projeto serviu como uma excelente oportunidade para aplicar os conceitos aprendidos no livro "Python Fluente", demonstrando como a escrita de código Pythonico pode resultar em:
- Código mais manutenível
- Melhor documentação
- Maior facilidade de leitura
- Melhor organização
- Código mais profissional

## 🚀 Como Usar

1. Coloque o script na pasta onde estão os arquivos .txt
2. Execute o script:
```bash
python main.py
```

O script irá:
1. Criar um arquivo `compilado.txt` com todo o conteúdo
2. Criar uma pasta `txt rip` para os arquivos originais
3. Mover todos os arquivos .txt originais para a pasta de backup

## 📖 Referências

- "Python Fluente" - Luciano Ramalho
- Documentação oficial do Python
- PEP 8 - Guia de Estilo para Código Python 