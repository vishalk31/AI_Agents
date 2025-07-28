import random

class TemperatureController:
    """
    A Reactive AI Agent for Temperature Control
    
    This agent demonstrates the basic SENSE → THINK → ACT cycle:
    - Maintains room temperature within acceptable range
    - Makes decisions based on current conditions only (no memory)
    - Takes immediate action to correct temperature deviations
    """
    
    def __init__(self):
        """Initialize the temperature controller with default settings"""
        self.target_temp = 24           # Desired room temperature (°C)
        self.tolerance = 2              # Acceptable deviation (±2°C comfort zone)
        self.current_temp = 30          # Starting temperature 
        self.current_action = "reduce"  # Initial action state
        
    def sense_temperature(self):
        """
        SENSE: Read current temperature from environment
        
        In real-world: would read from actual temperature sensor
        For simulation: generates random temperature between 21-33°C
        
        Returns:
            float: Current temperature reading
        """
        self.current_temp = random.randint(21, 33)
        return self.current_temp
    
    def decide_action(self):
        """
        THINK: Decide what action to take based on current temperature
        
        Decision Logic:
        - If temp > target + tolerance (>26°C): Cool down ("reduce")
        - If temp < target - tolerance (<22°C): Heat up ("increase") 
        - If within comfort zone (22-26°C): Do nothing ("remain_same")
        
        Returns:
            str: Action to take ("reduce", "increase", or "remain_same")
        """
        if self.current_temp > self.target_temp + self.tolerance:
            return "reduce"      # Too hot - need cooling
        elif self.current_temp < self.target_temp - self.tolerance:
            return "increase"    # Too cold - need heating
        else:
            return "remain_same" # Comfortable - no action needed
    
    def execute_action(self, action):
        """
        ACT: Execute the decided action and update temperature
        
        Action Effects:
        - "reduce": Instantly cool to upper comfort boundary (26°C)
        - "increase": Instantly heat to upper comfort boundary (26°C)  
        - "remain_same": No temperature change
        
        Args:
            action (str): The action to execute
        """
        self.action = action
        
        if self.action == "reduce":
            # Cool down to upper boundary of comfort zone
            self.current_temp = self.current_temp - (self.current_temp - (self.target_temp + self.tolerance))
        elif self.action == "increase":
            # Heat up to upper boundary of comfort zone
            self.current_temp = self.current_temp + ((self.target_temp + self.tolerance) - self.current_temp)
        else:
            # No action needed - temperature stays the same
            self.current_temp = self.current_temp
 
    def run_one_cycle(self):
        """
        Execute complete agent cycle: SENSE → THINK → ACT
        
        This is the main agent loop that demonstrates reactive behavior:
        1. Sense current conditions
        2. Think about what to do
        3. Act on the decision
        4. Report what happened
        
        Returns:
            float: Final temperature after the cycle
        """
        # SENSE: Get current temperature
        sense_current_temp = self.sense_temperature()
        
        # THINK: Decide what action to take
        decide_ac_action = self.decide_action()
        
        # ACT: Execute the chosen action
        execute_ac_action = self.execute_action(decide_ac_action)
        
        # REPORT: Show what the agent did
        print(f"Temperature: {self.current_temp}°C | Action: {self.action}")
        return self.current_temp

# ============================================
# DEMO: Watch the AI Agent in Action
# ============================================

if __name__ == "__main__":
    print("🤖 Temperature Control AI Agent Demo")
    print("=" * 40)
    print(f"Target: 24°C ± 2°C (Comfort zone: 22-26°C)")
    print()
    
    # Create and test the agent
    controller = TemperatureController()
    
    for i in range(5):
        print(f"Cycle {i+1}:")
        controller.run_one_cycle()
        print()
    
    print("🎉 Demo complete! Your first AI agent is working!")