import React, { Component } from 'react';

import Iframe from "./iframe.js"


class Grafana extends Component {
  constructor(props) {
    super(props);
    this.state = {draweropen: false,currentScreen:[]};
  }
  componentDidMount(){
   // var currentScreen=[];
   // currentScreen.push(<UploadScreen appContext={this.props.appContext} role={this.props.role}/>);
   // this.setState({currentScreen})
  }
  /**
   * Toggle opening and closing of drawer
   * @param {*} event 
   */ 
  toggleDrawer(event){
  // console.log("drawer click");
  this.setState({draweropen: !this.state.draweropen})
  }
 
  render() {
    return (
      <div className="Grafana" style={style}>
       
        <Iframe
                //url="http://www.youtube.com/embed/xDMP3i36naA"
                url="http://129.146.192.214:3001"
				width="1000px"
        height="1000px"
        type="application/json"
				id="myId"
			//	className="myClassname"
				display="initial"
				position="relative"
				allowFullScreen
			/>
      </div>
    );
  }
}
const style = {
  margin: 0,
  padding: 0,
  marginTop: 0,
  marginBottom: 5,
  marginLeft: 0,
  marginRight: 0,

  align: 'center'
};

export default Grafana;
