class GlueTemplate {
    constructor(unique_name, shared_context_data = {}) {
        this.unique_name = unique_name
        this.shared_context_data = shared_context_data
        this.event_dispatcher = new GlueEventDispatcher()
    }

    //Todo: Make sure there is not change of injection attack and get understanding of context data in templates

    async _render(context_data = {}) {
        return glue_ajax_request(this.unique_name, 'get', {...context_data, ...this.shared_context_data}, 'text/html');
    }

    render_inner(target_element, context_data = {}) {
        this._render(context_data).then((response) => {
            this.event_dispatcher.dispatch_response_event(response)
            return response.text()
        }).then((html) => {
            target_element.innerHTML = html
        })

    }

    render_outer(target_element, context_data = {}) {
        this._render(context_data).then((response) => {
            this.event_dispatcher.dispatch_response_event(response)
            return response.text()
        }).then((html) => {
            target_element.outerHTML = html
        })

    }

}