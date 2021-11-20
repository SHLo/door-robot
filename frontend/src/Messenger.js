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
    }
    this.handlePeopleChange = this.handlePeopleChange.bind(this);
    this.onClick = this.onClick.bind(this);
  }

  componentDidMount() {

  }

  onClick() {
    const dbPeopleRef = ref(db, '/people');
    onValue(dbPeopleRef, this.handlePeopleChange);
  }

  handlePeopleChange(snapshot) {
    const people = snapshot.val();
    let message = '';
    if (people && people.length > 0) {
      const names = people.map(person => person.name);
      console.log(names);
      const known = names.find(name => name !== 'stranger');

      if (!known) message = 'there is stranger at the door, please go check';
      else message = `${known} is back, I have unlocked the door`;
    }
    this.setState({ message });
    speak(message, 'en-US');
  }

  render() {
    return (
      <Alert variant='primary' onClick={this.onClick}>{this.state.message}</Alert>
    );
  }
}

export default Messenger;
