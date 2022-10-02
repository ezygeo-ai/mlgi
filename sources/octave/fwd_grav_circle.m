clc; clear all; close all;
% Parameter Model (rho,R,z,x0)
rho = 1;
% Perbedaan densitas (kg/m^3)
R = 10;
% Jari-jari (m)
z = 20;
% Kedalaman (m)
x0 = 10;
% Posisi model (m)
% Konstanta
cGrav = 6.674e-11; % Konstanta Gravitasi (m^3 kg^-1 s^-2)
si2mg = 1e5;
% 1 SI(ms^-2) = 1e5 mGal
% Lokasi Pengukuran
x = -100:10:100;
%%------- FORMULA FORWARD SPHERE ------%%
k = (4/3)*pi*cGrav*rho*(R^3);
for i = 1:length(x)
dg(i) = k*(z/((x(i)-x0)^2 + z^2)^(1.5)); % m s^2
end
dg = dg*si2mg;
% 1 SI = 1e5 mGal
%%--------- PLOT FORWARD -------%%
figure(1)
subplot(5,1,[1 2])
plot(x,dg,'.','color','r','MarkerSize',15);
xlim([min(x) max(x)]);
xlabel('\bf \fontsize{12}\fontname{Times}Posisi (m)');
ylabel('\bf \fontsize{12}\fontname{Times}\Delta g (mGal)');
title('\bf \fontsize{14}\fontname{Times}Modeling Gravity - Bola');
subplot(5,1,[4 5])
% Gambar Bola
th = 0:pi/50:2*pi;
xunit = R*cos(th)+x0;
yunit = R*sin(th)+z;
fill(xunit,yunit,'r');
set(gca,'ydir','reverse');
title(['\bf \fontsize{14}\fontname{Times}Model => ','\rho = ',...
num2str(rho),' kg/m^3 ; R = ',num2str(R),...
' m ; z = ',num2str(z),' m ; x_0 = ',num2str(x0),' m']);
xlabel('\bf \fontsize{12}\fontname{Times}Posisi (m)');
ylabel('\bf \fontsize{12}\fontname{Times}Kedalaman (m)');
xlim([min(x) max(x)]);
ylim([0 50]);
axis equal;