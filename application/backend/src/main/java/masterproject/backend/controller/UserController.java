package masterproject.backend.controller;




import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import masterproject.backend.model.EC2Instance;
import masterproject.backend.model.Login;
import masterproject.backend.model.UserInput;
import masterproject.backend.model.TriggerML;
import masterproject.backend.service.UserService;



@Controller
@CrossOrigin(origins = "*")
@RequestMapping(value = "/api")
public class UserController {

	@Autowired
	private UserService userService;

	@RequestMapping(value = "/login1", method = RequestMethod.POST)
	public ResponseEntity<String> login(@RequestBody UserInput userInput) {

		String message = userService.login(userInput);
		return new ResponseEntity<String>(message, HttpStatus.OK);
	}

	@RequestMapping(value = "/savetenancy", method = RequestMethod.POST)
	public ResponseEntity<String> saveTenancy(@RequestBody UserInput userInput) {
		System.out.println("Save tnenancy controller");

		String message = userService.saveTenancy(userInput);
		return new ResponseEntity<String>(message, HttpStatus.OK);
	}

	@RequestMapping(value = "/saveec2instance", method = RequestMethod.POST)
	public ResponseEntity<String> saveEC2Instance(@RequestBody UserInput userInput) {

		String message = userService.saveEC2Instance(userInput);
		return new ResponseEntity<String>(message, HttpStatus.OK);
	}

	@RequestMapping(value = "/list", method = RequestMethod.GET)
	public ResponseEntity<List<Login>> userDetails() {

		List<Login> userDetails = userService.getUserDetails();
		return new ResponseEntity<List<Login>>(userDetails, HttpStatus.OK);
	}

	@RequestMapping(value = "/register", method = RequestMethod.POST)
	public ResponseEntity<String> userDetails(@RequestBody UserInput userInput) {

		String message = userService.saveUserDetails(userInput);
		return new ResponseEntity<String>(message, HttpStatus.OK);
	}

	@RequestMapping(value = "/listall", method = RequestMethod.GET)
	public ResponseEntity<List<Login>> getUserDetailsAll() {

		List<Login> userDetails = userService.getUserDetailsAll();
		return new ResponseEntity<List<Login>>(userDetails, HttpStatus.OK);
	}

	@RequestMapping(value = "/ec2/id", method = RequestMethod.GET)
	public ResponseEntity<List<EC2Instance>> getUserDetailsById(@RequestParam(required = true) String userId) {

		List<EC2Instance> list  = userService.getEC2InstanceDetailsById(userId);

		return new ResponseEntity<List<EC2Instance>>(list, HttpStatus.OK);
	}

	@CrossOrigin(origins = "*")
	@RequestMapping(value = "/id/delete", method = RequestMethod.POST)
	public ResponseEntity<String> deleteEC2DetailsById(@RequestBody UserInput userInput) {
        System.out.println("deleteEC2DetailsById");
		userService.deleteEC2DetailsById(userInput);
		return new ResponseEntity<String>("Success", HttpStatus.OK);
	}


	@RequestMapping(value = "/trigger_ml", method = RequestMethod.POST)
	public ResponseEntity<String>  triggerML(@RequestBody TriggerML triggerML) {

		System.out.println("Trigger ML controller");
		String message = userService.triggerML(triggerML);
		return new ResponseEntity<String>(message, HttpStatus.OK);
	}

}
