<h1> Cadastro de Funcionários e Clientes - Projeto Django </h1>

Este é um projeto Django para gerenciar o cadastro de funcionários e clientes. Este tutorial irá guiá-lo através dos
passos necessários para configurar e executar o projeto em sua máquina local.

<h2> Pré-requisitos </h2>

Certifique-se de ter o seguinte instalado em sua máquina:

<ul>
    <li>
        Python (versão 3.x recomendada)
    </li>
    <li>
        pip (gerenciador de pacotes Python)
    </li>
    <li>
        Virtualvenv (opcional, mas altamente recomendado)
    </li>
</ul>

<h2> Passo 1: Clone do repositório </h2>

Clone o repositório do projeto em sua máquina local, via Git Bash:


<code> git clone https://github.com/analiceleite/projeto_crud_v2/edit/main/README.MD
cd projeto_crud_v2/ </code>


<h2>Passo 2: Instalação e configuração do PIP </h2>


<h3> Instalação do PIP no Windows </h3>

<strong>Abra um terminal, (No Terminal do VS Code): </strong>

-> Ctrl + Alt + T

Verifique se tem o PIP está instalado na máquina e qual a versão:

<code>pip -V</code>

<strong>Caso não encontre faça a instalação do PIP no Windows</strong>

Execute o comando abaixo no PowerShell (No Terminal do VS Code):

<code>pip install</code>

<strong>Após executar os comandos acima, reinicie o terminal, e verifique se o PIP está instalado e se precisa fazer uma
    atualização, neste caso você executa o seguinte comando</strong>

<strong>python.exe -m pip install --upgrade pip</strong>

<h4>Uma outra forma de instalar o pip e atualizar:</h4>

<code>pip install --upgrade pip</code>

<h3>Crie um ambiente virtual para instalação e configuração do seu projeto através das depedências e bibliotecas
    espefíficas.</h3>

O módulo usado para criar e gerenciar ambientes virtuais é chamado venv. O venv normalmente irá instalar a versão mais
recente de Python que você tiver disponível.

<i> Obs.: Ao clonar o repositório, é recomendado excluir a pasta venv e seguir este passo a passo para criar o ambiente
    virtual novamente, uma vez que no repositório clonado está o endereço da minha máquina local, dessa forma garantirá
    que a aplicação rode na sua máquina sem problemas de endereçamento. </i>

<code>py -m venv venv</code>

<strong>Após a criação da máquina virtual vcocê deverá ativar para continuar a configuração do seu projeto. Utilize o
    seguinte comando:</strong>

<strong>venv\Scripts\activate</strong>

Deverá aparecer (venv) em verde após e execução do código anterior.

<h3>Instalação do Django<h3>

<strong>Instale o Django usando o PIP (Python Package Installer). Execute o seguinte comando:</strong>

<strong>pip install Django</strong>

<strong>Verifique se a instalação foi bem-sucedida digitando o seguinte comando para exibir a versão do Django
instalada:</strong>

<strong>django-admin --version</strong>

<h3>Executando o Servidor</h3>

<strong>Utilize o comando abaixo para executar o projeto de aplicação web, digite no terminal:</strong>

<code>python manage.py runserver </code>

Se foi criado tudo certo até o momento, deverá ser executado indicando a seguinte mensagem no terminal.

<code>Django version ?.?.?, using settings 'clientes.settings'
Starting development server at http://127.0.0.1:8000/
</code>

Esse é o número do servidor web local(padrão) para abrir a aplicação web. Toda vez que precisar executar a
aplicação preciso iniciar o servidor.

<ul>
    <li>
        Verifique se o projeto está rodando:
    </li>
    <li>
        ágina inicial: http://localhost:8000
    </li>>
</ul>

<h3>Passo 6: Criar um Superusuário (Opcional)</h3>

Se precisar acessar o painel de administração do Django, crie um superusuário executando o seguinte comando:

<code>python manage.py createsuperuser
      Siga as instruções para criar o superusuário.</code>

Agora você configurou e está executando o projeto de cadastro de funcionários e clientes em sua máquina local.
Sinta-se à vontade para explorar e utilizar as funcionalidades do projeto!
