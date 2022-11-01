<template>
	<div class="date-range">
		<input class="date-input" type="date" id="start-date" value="">
		<input class="date-input" type="date" id="end-date" value="">
		<green-button
			class="date-input"
			@click="getDateRange"
		>
			Применить фильтр
		</green-button>
	</div>
</template>



<script>
export default {
	name: 'date-range',
	data() {
		return {
			dateStart: 0,
			dateEnd: 0,
			rangeLi: [],
		}
	},
	props: {
		liList: {
			type: Array,
			default: () => []
		}
	},
	methods: {
		getDateRange() {
			// Очищаем  список нужных ЛИ, если запускаем 2+ раз
			this.rangeLi = [];

			// Получаем даты начала и конца диапозона
			let dateStart = document.querySelector('#start-date').value + 'T00:00:00';
			let dateEnd = document.querySelector('#end-date').value + 'T00:00:00';
			this.dateStart = Date.parse(dateStart);
			this.dateEnd = Date.parse(dateEnd);

			// Пушим подходящие под условие ЛИ в список
			this.liList.forEach((val) =>
				(this.dateStart <= Date.parse(val['dt'])) && (Date.parse(val['dt']) <= this.dateEnd) ?
							this.rangeLi.push(val) :
							{/*pass*/});
			
			this.$emit('filterli', this.rangeLi)
		},
	},
	mounted() {
		document.querySelector('#end-date').valueAsDate = new Date();
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