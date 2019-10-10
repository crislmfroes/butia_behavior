# butia_behavior

Implementation of the main states and state machines used by the butia-bots
team in the Robocup's @home competition.

### States

- WaitTopic
    - outcomes: ['succeeded', 'error']

    Waits for a topic to be published.


### Machines

- boiler_plate

    Only uses the WaitHotword state. Used for development guidance purposes only.