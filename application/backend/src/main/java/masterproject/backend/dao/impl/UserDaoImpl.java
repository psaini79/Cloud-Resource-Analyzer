package masterproject.backend.dao.impl;

import java.sql.Date;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;

import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.springframework.stereotype.Repository;

import masterproject.backend.dao.UserDao;
import masterproject.backend.model.EC2Instance;
import masterproject.backend.model.Login;
import masterproject.backend.model.Tenancy;
import masterproject.backend.model.UserInput;
import masterproject.backend.utilities.DBConfig;


@Repository
public class UserDaoImpl implements UserDao {

	@PersistenceContext
    private EntityManager entityManager;
	
	public List<Login> getUserDetails() {
		//Criteria criteria = entityManager.createCriteria(UserDetails.class);
		
		SessionFactory sessionFactory = DBConfig.getSessionFactory();
		
		 Session session = sessionFactory.openSession();
		 
		 session.beginTransaction();
		 
		
		//session.createSQLQuery(hql).executeUpdate();
		  System.out.println("-- persisting persons --");
	     // System.out.printf("- %s%n- %s%n", p1, p2);
	      
	    //  session.save(p1);
	    //  session.save(p2);
	    //  session.save(p3);
	    //  session.getTransaction().commit();
		 
	      @SuppressWarnings("unchecked")
	      List<Login> persons = session.createQuery("FROM Login").list();
		
		System.out.println(persons.size());
		
		for(Login login:persons){
			
			System.out.println(login.getUserId());
			
		}
		
		return persons;
	}
	
	public void deleteEC2DetailsById(UserInput userInput){
		
		SessionFactory sessionFactory = DBConfig.getSessionFactory();

		Session session = sessionFactory.openSession();
		 session.beginTransaction();
		 String hql ="Delete FROM EC2Instance E WHERE E.id = :id";
			Query query = session.createQuery(hql);
			query.setParameter("id",Integer.parseInt(userInput.getEc2InstanceId()));

			
			int count3 = query.executeUpdate();
		  session.getTransaction().commit();
		 session.close();	
	}
	
public List<Login>  getUserDetailsAll(){
		
	SessionFactory sessionFactory = DBConfig.getSessionFactory();
		
		Session session = sessionFactory.openSession();
		String hql ="FROM Login E ";
		Query query = session.createQuery(hql);
		List<Login>  logins = query.list();
		 session.close();	
		return logins;
		
	}



public List<Login>  getUserDetailsById(String userId){
	
	SessionFactory sessionFactory = DBConfig.getSessionFactory();
		
		Session session = sessionFactory.openSession();
		String hql ="FROM Login E WHERE E.userId = :userId";
		Query query = session.createQuery(hql);
		query.setParameter("userId",userId);
		List<Login>  logins = query.list();
		 session.close();	
		return logins;
		
	}

public String saveUserDetails(UserInput userInput){
	
	SessionFactory sessionFactory = DBConfig.getSessionFactory();
	
	 Session session = sessionFactory.openSession();
	 
	 session.beginTransaction();
	
	 Login p1 = new Login(userInput.getFirstName(),userInput.getLastName(),userInput.getPassword(), userInput.getUserId(),userInput.getRole(),userInput.getDesignation(),userInput.getMobileNum());
	 Date date = Date.valueOf(LocalDate.now());
	 p1.setLastLogin(date);
	 p1.setCreatedOn(date);
	 
	  session.save(p1);
	  session.getTransaction().commit();
	  session.close();	
	  return "Success";  
}

public String saveTenancyDetails(UserInput userInput, Login login){
	
	SessionFactory sessionFactory = DBConfig.getSessionFactory();
	
	 Session session = sessionFactory.openSession();
	 
	 session.beginTransaction();
	
	/* String hql ="FROM Login E WHERE E.userId = :userId";
		Query query = session.createQuery(hql);
		query.setParameter("userId",userInput.getUserId());
		List<Login>  logins = query.list();
		if(logins== null || logins.size()==0){
		return "Error";
		}
	 login = logins.get(0);*/
	 Tenancy tenancy = new Tenancy(userInput.getTenancyName(),userInput.getCompanyName());
	 Date date = Date.valueOf(LocalDate.now());
	 tenancy.setCreatedOn(date);
	 login.setTenancy(tenancy);
	 
	  session.saveOrUpdate(login);
	  session.getTransaction().commit();
	  session.close();	
	  return "Success";  
}

public List<Login>  login(UserInput userInput){
	
	SessionFactory sessionFactory = DBConfig.getSessionFactory();
	Session session = sessionFactory.openSession();
	 session.beginTransaction();
	String hql ="FROM Login E WHERE E.userId = :userId and E.password = :password";
	Query query = session.createQuery(hql);
	query.setParameter("userId",userInput.getUserId());
	query.setParameter("password",userInput.getPassword());
	List<Login>  logins = query.list();
	 session.close();	
	return logins;
	
}

public String saveEC2Instance(UserInput userInput, Login login) {
	SessionFactory sessionFactory = DBConfig.getSessionFactory();
	
	 Session session = sessionFactory.openSession();
	 
	 session.beginTransaction();
	
	 String hql ="FROM Login E WHERE E.userId = :userId";
		Query query = session.createQuery(hql);
		query.setParameter("userId",userInput.getUserId());
		List<Login>  logins = query.list();
		if(logins== null || logins.size()==0){
		return "Error";
		}
	 login = logins.get(0);
	 EC2Instance ec2Instance = new EC2Instance(userInput.getEc2InstanceName());
	 //Date date = Date.valueOf(LocalDate.now());
	// tenancy.setCreatedOn(date);
	 List<EC2Instance> ec2InstanceList = new ArrayList<EC2Instance>();
	 
	 ec2InstanceList.add(ec2Instance);
	 ec2InstanceList.addAll(login.getTenancy().getEc2InstanceList());
	 
	 login.getTenancy().setEc2InstanceList(ec2InstanceList);
	 
	  session.saveOrUpdate(login);
	  session.getTransaction().commit();
	  session.close();	
	  return "Success"; 
}

public List<EC2Instance> getEC2InstanceDetailsById(String userId) {
	// TODO Auto-generated method stub
	SessionFactory sessionFactory = DBConfig.getSessionFactory();
	
	Session session = sessionFactory.openSession();
	String hql ="FROM Login E WHERE E.userId = :userId";
	Query query = session.createQuery(hql);
	query.setParameter("userId",userId);
	List<Login>  logins = query.list();
	
	List<EC2Instance> ec2list = new ArrayList<EC2Instance>();
	Tenancy tenancy = logins.get(0).getTenancy();
	if(tenancy != null){
		ec2list = tenancy.getEc2InstanceList();
	}
	
	
	List<EC2Instance> ec2listTemp = new ArrayList<EC2Instance>();
	for(EC2Instance ec2InstanceTemp : ec2list){
		
		EC2Instance ec2InstanceTemp1 = new EC2Instance();
		ec2InstanceTemp1.setEc2InstanceName(ec2InstanceTemp.getEc2InstanceName());
		ec2InstanceTemp1.setId(ec2InstanceTemp.getId());
		ec2listTemp.add(ec2InstanceTemp1);
		
	}

	
	
	 session.close();
	 return ec2listTemp;
}

}
