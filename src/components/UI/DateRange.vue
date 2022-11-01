<template>
	<div class="date-range">
		<input class="date-input" type="date" id="start-date">
		<input class="date-input" type="date" id="end-date">
		<green-button
			class="date-input"
			@click="filterByDate"
		>
			Отфильровать
		</green-button>
	</div>
</template>



<script>
export default {
	name: 'date-range',
	methods: {
		filterByDate() {
			let dateStart = document.querySelector('#start-date').value;
			let dateEnd = document.querySelector('#end-date').value;
			dateStart = Date.parse(dateStart);
			dateEnd = Date.parse(dateEnd);
			
			for (let i = dateStart; i <= dateEnd; i = i + 24*60*60*1000) {
				console.log(new Date(i).toISOString().slice(0, -5));
			}
		}
	}
}
</script>



<style scoped>
.date-range {
	display: flex;
	justify-content: center;
}
.date-input {
	margin: 15px 15px;
}
</style>