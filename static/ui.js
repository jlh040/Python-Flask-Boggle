class Request {
    constructor(url, data, headers) {
        this.url = url;
        this.data = data;
        this.headers = { headers} ;
    }

    async sendRequest() {
        await axios.post(this.url, this.data, this.headers);
    }

    async getResponseMessage() {
        const response = await axios.post(this.url, this.data, this.headers)
        return response.data.result;
    }
}
