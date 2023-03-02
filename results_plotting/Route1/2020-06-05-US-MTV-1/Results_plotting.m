clc;
clear;
% Plot the ground truth and set transformer based results
% Aaron (Xu Weng)
gt_file_name = "GT_set_transformer.csv";
setT_file_name = "Corrected_Position_set_transformer.csv";
GT_lla = load(gt_file_name);
setT_lla = load(setT_file_name);

figure1 = figure;
plot(GT_lla(:,3),GT_lla(:,2),'.','color','#008744','linewidth',2);hold on;
plot(setT_lla(:,3),setT_lla(:,2),'.','color','#D95319','linewidth',2);
legend("Ground Truth","Set Transformer");
xlabel("Longitude",'FontSize',40);
ylabel("Latitude",'FontSize',40);
axis tight;
axis([-122.5, -122.0, 37.3, 37.8]);
hold on;
I = imread('MTV.png'); 
h = image('XData',[-122.5, -122.0],'YData',[37.8,37.3],'CData',I);%note the latitude (y-axis) is flipped in vertical direction
uistack(h,'bottom'); %move the image to the bottom of current stack
saveas(figure1,'/Results_comparison.fig');