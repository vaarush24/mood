const happyButton = document.getElementById('happyButton');
const sadButton = document.getElementById('sadButton');
const neutralButton = document.getElementById('neutralButton');
const resultDiv = document.getElementById('result');

happyButton.addEventListener('click', () => showResult('happy'));
sadButton.addEventListener('click', () => showResult('sad'));
neutralButton.addEventListener('click', () => showResult('neutral'));

function showResult(mood) {
  resultDiv.textContent = `You are feeling ${mood} today.`;
}