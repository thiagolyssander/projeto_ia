%%%%%%%%%%%%%%%%%%%%%%%%%%
%limpeza de valores, tela e variaveis.
clc; close all; clear;

% carregando a biblioteca
pkg load image;

% carregando a imagem original
img = imread('semente.png');

% criação de um filtro de suavização 5x5 e aplicação na imagem.
filtro5x5= fspecial("average",5);
nova_imagem = imfilter(img, filtro5x5);

% convertendo a imagem para tons de cinza
img2 = rgb2gray(nova_imagem);

% detecção de bordas utilizando metodo de Prewitt
img3 = edge(img2, 'Prewitt');

% utilizando operações morfologicas para remoção de ruidos na imagem
SE = strel('square', 3);
img_dilate = imdilate(img3, SE);

% preenchimento de buracos na imagem
bw2 = imfill(img_dilate, 'holes');

% realizando operação para capturar individualmente cada semente.
cc = bwconncomp(bw2);
numPixels = cellfun(@numel, cc.PixelIdxList);

% variaveis onde podemos obter a semente com maior quantidade 
%de pixels e cada semente induvidual.
[biggest, idx] = max(numPixels);

% criação de nova matriz para armazenar a imagem e substituir
% a imagem original com cada semente individual e realizar o
% o processamento de cada uma.
rr = zeros(size(bw2));


% detecção da bordas das sementes
info = regionprops(cc,'BoundingBox');

# laço para gerar todas as 50 imagens individuais.
for k = 1 : 50
  rr(cc.PixelIdxList{k}) = 255;
  bb = info(k).BoundingBox;
  obj = imcrop(rr,bb);
  figure, imshow(obj);
end