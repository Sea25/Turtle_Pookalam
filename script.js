document.addEventListener('DOMContentLoaded', function() {
    
    createFlowers();
    
    
    const viewBtn = document.getElementById('viewBtn');
    viewBtn.addEventListener('click', showVideo);
});

function showVideo() {
    const videoContainer = document.getElementById('videoContainer');
    
    
    const video = document.createElement('video');
    video.controls = true;
    video.autoplay = true;
    
    
    const source = document.createElement('source');
    
    
    source.src = "img/pookalam.mp4";
    source.type = "video/mp4";
    
    
    video.appendChild(source);
    
    
    video.appendChild(document.createTextNode('Your browser does not support the video tag.'));
    
    videoContainer.innerHTML = '';
    videoContainer.appendChild(video);
    
    videoContainer.classList.add('show');
    
    videoContainer.scrollIntoView({ behavior: 'smooth' });
}

function createFlowers() {
    const container = document.body;
    const flowers = ['🌸', '🌺', '🌼', '🌷', '🌻', '💮'];
    
    for (let i = 0; i < 12; i++) {
        const flower = document.createElement('div');
        flower.className = 'flower';
        flower.innerHTML = flowers[Math.floor(Math.random() * flowers.length)];
        flower.style.left = Math.random() * 100 + '%';
        flower.style.animationDelay = Math.random() * 5 + 's';
        flower.style.animationDuration = (Math.random() * 10 + 10) + 's';
        container.appendChild(flower);
    }
}