# opencv
Estudos da biblioteca OpenCV

## Requisitos
<li>pip install opencv-contrib-python</li>
<li>pip install caer</li>

## Leitura de Imagens
<p>Método: <b>imread('caminho para img')</b></p>

## Mostrar Imagem
<p>Método: <b>imshow('nome_janela', var_matriz_pixels)</b></p>
<p>A imagem será aberta em uma nova janela.</p>

## Aguarda Pressionar Tecla
<p>Método: <b>waitKey(num_tecla)</b></p>

## Leitura de Vídeos
<p>Método: <b>VideoCapture('caminho_video')</b></p>
<p>Vale ressaltar que é possível também passar como parâmetro números inteiros de 0 a 2. Eles abrirão a Webcam do computador.</p>

## Mostrar Vídeos
<p>Utiliza-se o mesmo método que para as imagens (imshow). Porém, antes de inserir a variável nesse método, deve-se pegar uma instância de VideoCapture, e atribuir a outra variável, fazendo da seguinte forma: <b>var_nova = instanciaVideoCapture.read().</b></p>
<p>Assim, é só inserir no método imshow a nova variável junto ao parâmetro que dará nome à janela aberta.</p>

## Método destroyAllWindows
<p>Para finalizar o processo e fechar a(s) janela(s) aberta(s).</p>

