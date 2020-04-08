package masterproject.backend.model;


import java.sql.Date;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.OneToOne;
import javax.persistence.Table;

import com.fasterxml.jackson.annotation.JsonIgnore;

@Entity
@Table(name = "corp_tenancy_user_info")
public class Login {

	@Id
	@Column(name ="user_id")
	//@GeneratedValue(strategy = GenerationType.IDENTITY)
	private String userId;

	@Column(name ="first_name")
	private String firstName;
	@Column(name ="last_name")
	private String lastName;
	@Column(name ="email_id")
	private String emailId;
	@Column(name ="password")
	private String password;
	@Column(name ="role")
	private String role;

	
	@Column(name ="created_on")
	private Date createdOn;
		
	@Column(name ="last_login")
	private Date lastLogin;
	
	@Column(name ="designation")
	private String designation;
	//@Column(name ="tenancy_id")
	//private String tenancyId;
	
	@Column(name ="mobile_num")
	private String mobileNum;
	@JsonIgnore
	@OneToOne(cascade = {CascadeType.ALL})
	@JoinColumn(name="tenancy_id", nullable = true)
	private Tenancy tenancy;
	
		
	public String getUserId() {
		return userId;
	}

	public void setUserId(String userId) {
		this.userId = userId;
	}

	public String getFirstName() {
		return firstName;
	}

	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}

	public String getLastName() {
		return lastName;
	}

	public void setLastName(String lastName) {
		this.lastName = lastName;
	}

	public String getEmailId() {
		return emailId;
	}

	public void setEmailId(String emailId) {
		this.emailId = emailId;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public String getRole() {
		return role;
	}

	public void setRole(String role) {
		this.role = role;
	}

	public Date getCreatedOn() {
		return createdOn;
	}

	public void setCreatedOn(Date createdOn) {
		this.createdOn = createdOn;
	}

	public Date getLastLogin() {
		return lastLogin;
	}

	public void setLastLogin(Date lastLogin) {
		this.lastLogin = lastLogin;
	}

	public String getDesignation() {
		return designation;
	}

	public void setDesignation(String designation) {
		this.designation = designation;
	}

	public String getMobileNum() {
		return mobileNum;
	}

	public void setMobileNum(String mobileNum) {
		this.mobileNum = mobileNum;
	}

	public Login(){
		
	}
	
	public Login(String firstName, String lastName,String password,String userId,String role,String designation,String mobileNum){
		this.firstName= firstName;
		this.lastName= lastName;		
		this.password= password;
		this.userId= userId;
		
		this.role= role;
		this.designation= designation;
		this.mobileNum= mobileNum;
	}

	public Tenancy getTenancy() {
		return tenancy;
	}

	public void setTenancy(Tenancy tenancy) {
		this.tenancy = tenancy;
	}
	
}
