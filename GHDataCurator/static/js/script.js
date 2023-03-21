function toggleSwitches(mainSwitch) {
    let switches = document.querySelectorAll('.form-check-input[type="checkbox"]:not(#mainSwitch)');
    for (let i = 0; i < switches.length; i++) {
      switches[i].checked = mainSwitch.checked;
    }
  }
  
  function checkSwitches(notMainSwitch) {
    let switches = document.querySelectorAll('.form-check-input[type="checkbox"]:not(#mainSwitch)');
    let allSwitchesOn = true;
    
    for (let i = 0; i < switches.length; i++) {
      if (!switches[i].checked) {
        allSwitchesOn = false;
        break;
      }
    }
    
    if (allSwitchesOn) {
      mainSwitch.checked = true;
    } else {
      mainSwitch.checked = false;
    }
  }
  