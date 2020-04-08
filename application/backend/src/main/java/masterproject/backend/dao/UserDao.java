package masterproject.backend.dao;

import java.util.List;

import masterproject.backend.model.EC2Instance;
import masterproject.backend.model.Login;
import masterproject.backend.model.UserInput;

public interface UserDao {
	
	List<Login> getUserDetails();
	
	List<Login> getUserDetailsById(String userId);
	
	List<Login>  getUserDetailsAll();
	
	String saveUserDetails(UserInput userInput);
	
	List<Login> login(UserInput userInput);
	
	void deleteEC2DetailsById(UserInput userInput);

	String saveTenancyDetails(UserInput userInput, Login login);

	String saveEC2Instance(UserInput userInput, Login login);

	List<EC2Instance> getEC2InstanceDetailsById(String userId);

}
