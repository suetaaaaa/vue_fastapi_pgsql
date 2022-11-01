<template>
	<div class="app">
		<date-range
			:liList="liForDateRange"
			@filterli="filterLi"
		/>
		<my-select
			v-model="selectedSort"
			:options="sortOptions"
		/>
		<li-table
			:li="sortedLi"
			:key="li.id"
			
		/>
	</div>
</template>



<script>
import axios from 'axios';

export default {
    data() {
        return {
            li: [],
			liForDateRange: [],
			isLiLoading: false,
			selectedSort: '',
			sortOptions: [
				{value: 'name', name: 'По названию'},
				{value: 'dt', name: 'По дате'},
				{value: 'code', name: 'По коду'},
			]
        };
    },
	methods: {
		async fetchLi() {
			try {
				this.isLiLoading = true;
				const response = await axios.get('http://127.0.0.1:1337/li');
				this.li = response.data;
				this.liForDateRange = response.data;
			} catch (e) {
				alert(e);
			} finally {
				this.isLiLoading = false;
			}
		},
		filterLi(rangeLi) {
			this.li = rangeLi;
		}
	},
	mounted() {
		this.fetchLi();
	},
	computed: {
		sortedLi() {
			return [...this.li].sort((li1, li2) => li1[this.selectedSort]?.localeCompare(li2[this.selectedSort]))
		}
	},
}
</script>



<style>
* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
}

.app {
	padding: 20px;
}
</style>
