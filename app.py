from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return """
	<!DOCTYPE html>
	<html>
	<body style="text-align:center;font-family:sans-serif; padding-top:50px;">
		<h1>Dolphin Facts!<h1>
		<p id="fact">Click the button for a dolphin fact.</p>
		<button onclick ="showFact()">Show Next Fact</button>

		<script>
			function showFact() {
				const facts = [
					"Dolphins use signiture whistles to call each other by name.",
					"Dolphins don't drink water because they get it from the food they eat.",
					"Dolphins eat around 35 pounds of fish every day.",
					"Dolphins usually travel in pods of up to 1,000 individuals."
				];
				const randomFact = facts[Math.floor(Math.random() * facts.length)];
				document.getElementById('fact').innerText = randomFact;
			}
		<script>
	</body>
	<html>
	"""
