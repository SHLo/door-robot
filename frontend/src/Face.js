function Face() {
  return (
    <div className="App">
      <header className="App-header">
        <svg height="600" width="1424" viewBox="100 0 200 300">
          <rect x="0" y="0" width="400" height="250" fill="#808080" stroke="#000000" />
          <circle cx="100" cy="100" r="40" fill="none" stroke="#000000" />
          <circle class="inner-eyelid" cx="100" cy="100" r="30" fill="#FFFFFF" stroke="#000000" />

          <rect x="190" y="120" width="20" height="50" fill="#FFFFFF" stroke="#000000" />

          <circle cx="300" cy="100" r="40" fill="none" stroke="#000000" />
          <circle class="inner-eyelid" cx="300" cy="100" r="30" fill="#FFFFFF" stroke="#000000" />

          <rect x="100" y="200" width="200" height="20" fill="#FFFFFF" stroke="#000000" />
          <line x1="100" y1="100" x2="100" y2="100" stroke="#FF0000" stroke-width="2px" />
          <line x1="300" y1="100" x2="300" y2="100" stroke="#FF0000" stroke-width="2px" />
        </svg>
      </header>

    </div>
  );
}

export default Face;
