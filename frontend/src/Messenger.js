import Alert from 'react-bootstrap/Alert'
import React from 'react';
import { db } from './firebase';
import { ref, onValue } from "firebase/database";
import speak from './speak';

class Messenger extends React.Component {
  constructor() {
    super();
    this.state = {
      message: 'Please click to start',
      busy: false,
    }
    this.handlePeopleChange = this.handlePeopleChange.bind(this);
    this.handlePackagesChange = this.handlePackagesChange.bind(this);
    this.onClick = this.onClick.bind(this);
    const recognition = new window.webkitSpeechRecognition();
    recognition.continous = true;
    recognition.interimResults = false;
    recognition.lang = "en-US";
    this.recognition = recognition;
  }

  componentDidMount() {

  }

  onClick() {
    const dbPeopleRef = ref(db, '/people');
    onValue(dbPeopleRef, this.handlePeopleChange);

    const dbPackagesRef = ref(db, '/packages');
    onValue(dbPackagesRef, this.handlePackagesChange);
  }

  async handlePeopleChange(snapshot) {
    if (this.state.busy) return;

    const people = snapshot.val();

    if (!people || people.length <= 0) return;
    this.setState({ busy: true });

    let message = '';
    const names = people.map(person => person.name);
    console.log(names);
    const known = names.find(name => name !== 'stranger');

    if (!known) message = 'there is stranger at the door, please go check';
    else message = `${known} is back, I have unlocked the door`;

    this.setState({ message });
    await speak(message, 'en-US');

    if (!known) {
      message = 'do you want me to open the door for this guest?';
      this.setState({ message });
      await speak(message, 'en-US');
      this.recognition.start();
      this.recognition.onresult = (event) => {
        const inputSpeech = event.results[0][0].transcript;
        console.log(`recognition: ${inputSpeech}`);
        this.recognition.stop();
        if (inputSpeech.toLowerCase().includes('yes')) {
          message = 'got it, I have unlocked the door';
        } else {
          message = 'OK, I will not unlock the door';
        }
        this.setState({ message });
        speak(message, 'en-US');

      };
    }
    this.setState({ busy: false });
  }

  handlePackagesChange(snapshot) {
    if (this.state.busy) return;
    this.setState({ busy: true });
    const packages = snapshot.val();
    console.log(packages);
    let message = '';
    if (packages > 0) {
      if (packages === 1) message = 'you have a package to pick up';
      else message = `you have ${packages} packages to pick up`;
    }
    this.setState({ message });
    speak(message, 'en-US');
    this.setState({ busy: false });
  }

  render() {
    return (
      <Alert variant='primary' onClick={this.onClick}>{this.state.message}</Alert>
    );
  }
}

export default Messenger;
