load("../../../datasets/SIDD/ValidationGtBlocksSrgb.mat");
load('../../../datasets/SIDD/ValidationNoisyBlocksSrgb.mat');

for i = 1:40
    for j = 1:32
        input = squeeze(ValidationNoisyBlocksSrgb(i, j, :, :, :));
        target = squeeze(ValidationGtBlocksSrgb(i, j, :, :, :));
        imwrite(input, ['../../../datasets/SIDD/valid/input/original/' num2str(i,'%04d') '_noisy_srgb_' num2str(j,'%03d') '.png']);
        imwrite(target, ['../../../datasets/SIDD/valid/target/original/' num2str(i,'%04d') '_gt_srgb_' num2str(j,'%03d') '.png']);
    end
end
