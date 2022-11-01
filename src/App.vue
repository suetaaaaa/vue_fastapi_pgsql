<template>
	<div class="app">
		<DateRange/>
		<MySelect
			v-model="selectedSort"
			:options="sortOptions"
		/>
		<LiTable
			:li="sortedLi"
			:key="li.id"
		/>
	</div>
</template>



<script>
import axios from 'axios';

import LiTable from './components/LiTable.vue';
import DateRange from './components/UI/DateRange.vue';
import MySelect from './components/UI/MySelect.vue';


export default {
	components: {
    LiTable,
    DateRange,
    MySelect
},
    data() {
        return {
            li: [],
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
			} catch (e) {
				alert(e);
			} finally {
				this.isLiLoading = false;
			}
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
	// watch: {
	// 	selectedSort(newValue) {
	// 		this.li.sort((li1, li2) => {
	// 			return li1[newValue]?.localeCompare(li2[newValue])
	// 		})
	// 	}
	// }
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
