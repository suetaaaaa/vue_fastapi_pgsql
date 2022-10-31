<template>
	<div class="app">
		<green-button
			@click="fetchLi"
		>
			Загрузить ЛИ
		</green-button>
		<LiTable/>
	</div>
</template>



<script>
import LiTable from './components/LiTable.vue';
import axios from 'axios';

export default {
	components: {
		LiTable
	},
    data() {
        return {
            li: [],
			isLiLoading: false,
        };
    },
	methods: {
		async fetchLi() {
			try {
				this.isLiLoading = true;
				const response = await axios.get('http://127.0.0.1:1337/li');
				this.li = response.data;
				console.log(response.data);
			} catch (e) {
				alert(e);
			} finally {
				this.isLiLoading = false;
			}
		}
	},
	mounted() {
		this.fetchLi();
	}
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
