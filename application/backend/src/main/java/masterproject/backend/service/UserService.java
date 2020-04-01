package masterproject.backend.service;

import java.util.List;

import masterproject.backend.model.EC2Instance;
import masterproject.backend.model.Login;
import masterproject.backend.model.UserInput;

public interface UserService {

	List<Login> getUserDetails();

	List<Login> getUserDetailsAll();

	String saveUserDetails(UserInput userInput);

	String login(UserInput userInput);

	String saveTenancy(UserInput userInput);

	List<Login> getUserDetailsById(String userId);

	void deleteEC2DetailsById(UserInput userInput);

	String saveEC2Instance(UserInput userInput);

	List<EC2Instance> getEC2InstanceDetailsById(String userId);

}
