package masterproject.backend.service.impl;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import masterproject.backend.dao.UserDao;
import masterproject.backend.model.EC2Instance;
import masterproject.backend.model.Login;

import masterproject.backend.model.UserInput;
import masterproject.backend.service.UserService;

@Service
public class UserServiceImpl implements UserService {

	@Autowired
	private UserDao userDao;


	public List<Login> getUserDetails() {
		return userDao.getUserDetails();

	}

	public String login(UserInput userInput) {

		List<Login> login = userDao.login(userInput);
		String message = "Error";
		if (login != null && login.size() == 0) {
			message = "User Id or Password is InCorrect";
		} else if (login.size() == 1) {
			message = "Success";
		}
		return message;
	}

	public String saveTenancy(UserInput userInput) {
		List<Login> loginlist = userDao.getUserDetailsById(userInput.getUserId());
		String message = "Error";
		if (loginlist != null && loginlist.size() > 0) {
			Login login = loginlist.get(0);

			message = userDao.saveTenancyDetails(userInput, login);
		}
		return message;

	}

	public String saveEC2Instance(UserInput userInput) {
		List<Login> loginlist = userDao.getUserDetailsById(userInput.getUserId());
		String message = "Error";
		if (loginlist != null && loginlist.size() > 0) {
			Login login = loginlist.get(0);

			message = userDao.saveEC2Instance(userInput, login);
		}
		return message;
	}

	/*
	 * public List<Register> getRegisterDetails() { //Login login =
	 * userDao.getUserDetailsById("Raji@gmail.com"); //return
	 * registerDao.getRegisterDetails(login);
	 * 
	 * }
	 */

	public String saveUserDetails(UserInput userInput) {
		List<Login> login = userDao.getUserDetailsById(userInput.getUserId());
		String message = "Error";
		if (login != null && login.size() > 0) {
			message = "User Id is already available. Please enter different User Id.";
		} else {
			message = userDao.saveUserDetails(userInput);
		}
		return message;
	}

	public List<Login> getUserDetailsAll() {
		return userDao.getUserDetailsAll();

	}

	public List<Login> getUserDetailsById(String userId) {
		return userDao.getUserDetailsById(userId);
	}

	public void deleteEC2DetailsById(UserInput userInput) {
		// TODO Auto-generated method stub
		userDao.deleteEC2DetailsById(userInput);
	}

	public List<EC2Instance> getEC2InstanceDetailsById(String userId) {
		// TODO Auto-generated method stub
		return userDao.getEC2InstanceDetailsById(userId);
	}

}
