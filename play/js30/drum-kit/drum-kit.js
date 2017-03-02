

function removeTransition(x) {
	//console.log(x);
	if (x.propertyName !== 'transform') return;
	console.log(x.propertyName);
	x.target.classList.remove('playing');

}

function playSound(x) {
	// select where data-key == key pressed
	const audio = document.querySelector(`audio[data-key="${x.keyCode}"]`);
	// audio animation
	const key = document.querySelector(`.key[data-key="${x.keyCode}"]`);
	if(!audio) return;   // halt if no audio
	
	key.classList.add('playing');
	audio.currentTime = 0; // rewind to start
	audio.play();
}

const keys = Array.from(document.querySelectorAll('.key'));
keys.forEach(key => key.addEventListener('transitionend', removeTransition));
window.addEventListener('keydown', playSound);
