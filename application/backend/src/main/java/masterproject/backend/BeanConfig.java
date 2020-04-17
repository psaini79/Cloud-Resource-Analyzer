package masterproject.backend;



import javax.sql.DataSource;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.jdbc.datasource.DriverManagerDataSource;


@Configuration
public class BeanConfig {

//	@Bean
//    ServletRegistrationBean h2servletRegistration(){
//        ServletRegistrationBean registrationBean = new ServletRegistrationBean(new WebServlet());
//        registrationBean.addUrlMappings("/console/*");
//        return registrationBean;
//    }
	
	
    @Bean
    public DataSource dataSource(){
       DriverManagerDataSource dataSource = new DriverManagerDataSource();
       dataSource.setDriverClassName("org.postgresql.Driver");
       dataSource.setUrl("jdbc:postgresql://pg-prometheus-0.pg-prometheuss-lb.default.svc.cluster.local:5432/postgres");
      // dataSource.setUrl("jdbc:postgresql://localhost:5432/postgres");
       dataSource.setUsername( "postgres" );
       dataSource.setPassword( "mypass" );
       return dataSource;
    }

}
