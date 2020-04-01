package masterproject.backend.utilities;



import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class DBConfig {
	

	 private static SessionFactory factory =null; 
	 
	 
	 public static SessionFactory getSessionFactory(){
		 if(factory == null){
			 factory =  new Configuration().configure().buildSessionFactory();
		 }
		 return factory;
	 }
	
	private DBConfig(){
		
	}

}
