document.addEventListener("DOMContentLoaded", function() {
    const fileInputs = document.querySelectorAll('input[type="file"]');

    fileInputs.forEach(function(input) {
        const previewImg = document.createElement('img');
        previewImg.style.maxWidth = '300px';
        previewImg.style.maxHeight = '300px';
        previewImg.style.marginTop = '10px';
        previewImg.style.borderRadius = '8px';
        previewImg.style.display = 'none';

        input.parentNode.insertBefore(previewImg, input.nextSibling);

        input.addEventListener('change', function() {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    previewImg.src = e.target.result;
                    previewImg.style.display = 'block';
                }
                reader.readAsDataURL(file);
            } else {
                previewImg.style.display = 'none';
            }
        });
    });
});