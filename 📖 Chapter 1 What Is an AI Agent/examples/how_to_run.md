# How to Run the Temperature Controller Agent

## 🚀 Quick Start

1. **Save the code** as `temperature_controller.py`
2. **Run it** with: `python temperature_controller.py`
3. **Watch** your AI agent control temperature in real-time!

## 📖 What You'll See
🤖 Temperature Control AI Agent Demo
Target: 24°C ± 2°C (Comfort zone: 22-26°C)
Cycle 1:
Temperature: 28°C | Action: reduce
Cycle 2:
Temperature: 23°C | Action: remain_same
Cycle 3:
Temperature: 21°C | Action: increase

## 🎯 Understanding the Output

- **Temperature**: Current room temperature the agent sensed
- **Action**: What the agent decided to do
  - `reduce` = Cooling (AC on)
  - `increase` = Heating (heater on)  
  - `remain_same` = Comfortable (systems idle)

## 🛠️ Customizing Your Agent

Want to experiment? Change these values in the code:

self.target_temp = 24    # Change to your preferred temperature
self.tolerance = 2       # Change comfort zone size
🧪 Try These Experiments

Hot Room: Change random.randint(21, 33) to random.randint(27, 35)
Cold Room: Change to random.randint(15, 25)
Narrow Comfort: Change self.tolerance = 1
Wide Comfort: Change self.tolerance = 5

🐛 Troubleshooting
Problem: Import error with random
Solution: Make sure you have Python installed correctly
Problem: Agent always shows same action
Solution: The temperature range might be too narrow - try expanding it
🎓 What This Teaches
This simple agent demonstrates:

Reactive behavior (responds to current conditions)
SENSE-THINK-ACT cycle (the foundation of all AI agents)
Rule-based decisions (if-then logic)
Real-time adaptation (changes behavior based on environment)