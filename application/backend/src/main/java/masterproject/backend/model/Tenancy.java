package masterproject.backend.model;

import java.sql.Date;
import java.util.List;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.OneToMany;
import javax.persistence.OneToOne;
import javax.persistence.Table;

import com.fasterxml.jackson.annotation.JsonIgnore;

@Entity
@Table(name = "Tenancy")
public class Tenancy {
	
	@Id
	@Column(name ="id")
	@GeneratedValue(strategy = GenerationType.IDENTITY)
    private String id;
	
	@Column(name ="tenancy_name")
	private String tenancyName;
	@Column(name ="created_on")
	private Date createdOn;
	@Column(name ="company_name")
	private String companyName;
	
	@JsonIgnore
	 @OneToOne(mappedBy = "tenancy", fetch = FetchType.LAZY)
	// @PrimaryKeyJoinColumn
	 private Login login;
	@JsonIgnore
	 @OneToMany(cascade = {CascadeType.ALL})
	 @JoinColumn(name="ec2Instance_Id")
	 private List<EC2Instance> ec2InstanceList;


	 public Tenancy(){

		}

		public Tenancy(String tenancyName, String companyName){
			this.tenancyName=tenancyName;
			this.companyName=companyName;
		}


		public String getId() {
			return id;
		}


		public void setId(String id) {
			this.id = id;
		}


		public String getTenancyName() {
			return tenancyName;
		}


		public void setTenancyName(String tenancyName) {
			this.tenancyName = tenancyName;
		}


		public Date getCreatedOn() {
			return createdOn;
		}


		public void setCreatedOn(Date createdOn) {
			this.createdOn = createdOn;
		}


		public String getCompanyName() {
			return companyName;
		}


		public void setCompanyName(String companyName) {
			this.companyName = companyName;
		}


		public Login getLogin() {
			return login;
		}


		public void setLogin(Login login) {
			this.login = login;
		}

		public List<EC2Instance> getEc2InstanceList() {
			return ec2InstanceList;
		}

		public void setEc2InstanceList(List<EC2Instance> ec2InstanceList) {
			this.ec2InstanceList = ec2InstanceList;
		}

}
