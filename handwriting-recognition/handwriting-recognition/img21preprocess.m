function img = img21preprocess()
selected_col=50;
selected_ln=50;
I=imread("txtimg10.png");
Igray = rgb2gray(I);
%Igray=I;
Ibw = im2bw(Igray,graythresh(Igray));
Icomp=imcomplement(Ibw);
I2=imcomplement(Igray);
Ifill=Icomp;
[Ilabel num] = bwlabel(Ifill);
Iprops = regionprops(Ilabel);
Ibox = [Iprops.BoundingBox];
[y,x]=size(Ibox);
x=x/4;
Ibox = reshape(Ibox,[4 x]);
for cnt=1:x
    img{cnt} =  imcrop(I2,Ibox(:,cnt) );
    img{cnt} = imresize(img{cnt},[selected_col selected_ln]);
    
end
f=fopen('fed1num.txt','a');
for i=1:cnt
        for j=1:selected_col
            for k=1:selected_ln
                fprintf(f,'%f ' ,img{i}(j,k));
            end
        end
        fprintf(f,'\n');
end
fclose(f);
end