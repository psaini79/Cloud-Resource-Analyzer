package masterproject.backend.model;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;

import com.fasterxml.jackson.annotation.JsonIgnore;

@Entity
@Table(name = "ec2_instance_info")
public class EC2Instance {
//
//	@Id
//	@Column(name ="Id")
//	@GeneratedValue(strategy = GenerationType.IDENTITY)
//	private String id;
//
//	@Column(name ="ec2InstanceName")
//	private String ec2InstanceName;
//
//	@JsonIgnore
//	 @ManyToOne(cascade = {CascadeType.ALL})
//	    @JoinColumn(name="ec2Instance_Id")
//	    private Tenancy tenancy;

	@Id
	@Column(name = "id")
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private String id;

	@Column(name = "ec2instanceName")
	private String ec2InstanceName;

	// @JsonIgnore
	// @ManyToOne(cascade = {CascadeType.ALL})

	@JoinColumn(name="tenancy_id")
		@ManyToOne()
		private Tenancy tenancy;

	public EC2Instance() {

	}

	public EC2Instance(String ec2InstanceName) {
		this.ec2InstanceName = ec2InstanceName;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getEc2InstanceName() {
		return ec2InstanceName;
	}

	public void setEc2InstanceName(String ec2InstanceName) {
		this.ec2InstanceName = ec2InstanceName;
	}

	public Tenancy getTenancy() {
		return tenancy;
	}

	public void setTenancy(Tenancy tenancy) {
		this.tenancy = tenancy;
	}

}
