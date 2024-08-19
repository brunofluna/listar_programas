# Importar biblioteca
import winapps

for item in winapps.list_installed():
    print(f'Programa: {item.name}.')
    print(f'Versão: {item.version}.')
    print(f'Data de Instalação: {item.install_date}.')
    print(f'Data de Publicação: {item.publisher}.')
    print(f'Programa: {item.uninstall_string}.')
    print('-'*50)