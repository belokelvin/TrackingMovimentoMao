# Detecção de Mãos e Rastreamento do Dedo Indicador

Este é um código Python que utiliza a biblioteca MediaPipe para detectar mãos em um fluxo de vídeo da webcam e rastrear o movimento do dedo indicador. Ele exibe o vídeo da webcam em tempo real e desenha as landmarks das mãos e as linhas que acompanham o movimento do dedo indicador na imagem.

## Requisitos de Instalação

Antes de executar o código, é necessário instalar algumas bibliotecas Python. Você pode fazer isso facilmente usando o pip. Certifique-se de ter o pip instalado em seu sistema. Caso não tenha, instale o Python e o pip a partir do site oficial (https://www.python.org/).

Execute o seguinte comando para instalar as bibliotecas necessárias:

```bash
pip install numpy opencv-python mediapipe
```

## Como Usar

Após a instalação das bibliotecas, você pode executar o código da seguinte maneira:

```bash
python nome_do_arquivo.py
```

Isso iniciará o programa e abrirá uma janela que exibirá o vídeo da webcam em tempo real com as landmarks das mãos e o rastreamento do dedo indicador.

## Funcionamento do Código

O código começa importando as bibliotecas necessárias, incluindo `numpy`, `opencv`, `mediapipe` e outras.

Em seguida, ele cria um objeto `Hands` da biblioteca MediaPipe, configurando as confianças mínimas necessárias para a detecção e o rastreamento das mãos.

A captura de vídeo da webcam é iniciada e um loop é executado para processar cada quadro de vídeo. Durante o loop, o código detecta mãos na imagem e desenha as landmarks das mãos e as conexões entre elas usando as configurações especificadas.

Além disso, o código rastreia o movimento do dedo indicador (índice 8) e desenha linhas para acompanhar seu movimento na imagem.

O programa é encerrado ao pressionar a tecla "Esc".

## Contribuição

Este código foi desenvolvido para fins educacionais e de demonstração. Sinta-se à vontade para contribuir, melhorar e adaptar conforme suas necessidades.

## Autor

Este código foi escrito por Kelvin Belo e faz parte de um projeto para demonstrar a detecção de mãos e o rastreamento do dedo indicador com a biblioteca MediaPipe.

Divirta-se experimentando e explorando a detecção de mãos e o rastreamento do dedo indicador!
