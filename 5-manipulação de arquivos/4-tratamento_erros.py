from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    arq = open(ROOT_PATH / 'novo-diretorio' / "new.txt", 'r')
except FileNotFoundError as exc:
    print('arquivo não encontrado')
    print(exc)
except IsADirectoryError as exc:
    print(f'não foi possivel abrir o arquivo {exc}')
except IOError as exc:
    print(f'erro ao abrir o arquivo {exc}')
except Exception as exc:
    print(f'ocorreu algum problema ao abrir o arquivo {exc}')




