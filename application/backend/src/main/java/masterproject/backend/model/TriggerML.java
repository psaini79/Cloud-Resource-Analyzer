package masterproject.backend.model;

public class TriggerML {

	String userId;
	String period;
	String model;
	public String getUserId() {
		return userId;
	}
	public void setUserId(String userId) {
		this.userId = userId;
	}
	public String getPeriod() {
		return period;
	}
	public String getModel() {
		return model;
	}
	public void setModel(String model) {
		this.model = model;
	}
	public void setPeriod(String period) {
		this.period = period;
	}

	
	@Override
	public String toString() {
		
		return "model =" + getModel() + " period =" + getPeriod();
		
	}


}
