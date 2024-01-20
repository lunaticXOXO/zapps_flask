export default class Login {
  constructor() {
    this.KEY = "your_secret_key";
    this.username = ""
    this.id = null
  }

  getCurrentUserType() {
    console.log("Get Item: ", JSON.parse(localStorage.getItem(this.KEY)))
    return JSON.parse(localStorage.getItem(this.KEY)) || 'Guest';
  }

  getCurrentUsername(){
    console.log("Get Username: ", JSON.parse(localStorage.getItem(this.username)))
    return JSON.parse(localStorage.getItem(this.username)) || 'Guest';
  }

  getID(){
    console.log("Get ID: ", JSON.parse(localStorage.getItem(this.id)))
    return JSON.parse(localStorage.getItem(this.id)) || 'Guest';
  }

  addToUserType(userType) {
    const currentUserType = JSON.parse(localStorage.getItem(this.KEY)) || [];
    currentUserType.push(userType);
    localStorage.setItem(this.KEY, JSON.stringify(currentUserType[0]));
  }
  
  addToID(id){
    const currentID = JSON.parse(localStorage.getItem(this.id)) || [];
    currentID.push(id);
    console.log("Set id: ", this.id, JSON.stringify(currentID[0]))
    localStorage.setItem(this.id, JSON.stringify(currentID[0]));
  }

  addToUsername(username) {
    const currentUsername = JSON.parse(localStorage.getItem(this.username)) || [];
    currentUsername.push(username);
    console.log("Set username: ", this.username, JSON.stringify(currentUsername[0]))
    localStorage.setItem(this.username, JSON.stringify(currentUsername[0]));
  }

  

  removeUserType() {
    localStorage.removeItem(this.KEY)
    localStorage.clear()
  }
}