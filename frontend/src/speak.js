async function speak(text, lang) {
  /*Check that your browser supports text to speech*/
  if ('speechSynthesis' in window) {
    const msg = new SpeechSynthesisUtterance();
    const voices = window.speechSynthesis.getVoices();
    if (voices.length > 0) {
      msg.voice = voices.filter(function (voice) {
        return voice.lang === lang;
      })[1];
    }
    msg.voiceURI = 'native';
    msg.volume = 0.8; // 0 to 1
    msg.rate = 0.8; // 0.1 to 10
    msg.pitch = 0.8; //0 to 2
    msg.text = text;
    msg.lang = lang;
    msg.onend = function (e) {
      console.log('Finished in ' + e.elapsedTime + ' milliseconds.');
    };
    speechSynthesis.speak(msg);

    return new Promise(resolve => {
      msg.onend = resolve;
    });
  }
}

export default speak;

