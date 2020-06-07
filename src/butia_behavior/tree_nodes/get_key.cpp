#include "behaviortree_cpp_v3/behavior_tree.h"
#include "ros/ros.h"
#include "butia_world_msgs/GetKey.h"
#include "stdlib.h"

class GetKeyAction : public BT::SyncActionNode
{
    private:
        std::string service;
        ros::ServiceClient client;
        ros::NodeHandle n;

    public:
        GetKeyAction(const std::string &name, const BT::NodeConfiguration &config) : BT::SyncActionNode(name, config)
        {
            
        }

        static BT::PortsList providedPorts()
        {
            return {
                BT::InputPort<std::string>("method"),
                BT::InputPort<std::string>("query"),
                BT::OutputPort<std::string>("key")
            };
        }

        BT::NodeStatus tick() override
        {
            auto methodOptional = this->getInput<std::string>("method");
            auto queryOptional = this->getInput<std::string>("query");
            std::string method = "closest";
            if (methodOptional) {
                method = methodOptional.value();
            }
            if (!queryOptional) {
                throw BT::RuntimeError("missing required input [query]: ", queryOptional.error());
            }
            std::string query = queryOptional.value();
            sprintf(this->service.data(), "/butia_world/get_%s_key", method);
            this->client = n.serviceClient<butia_world_msgs::GetKey>(this->service);
            this->client.waitForExistence();
            butia_world_msgs::GetKey srv;
            srv.request.query = query;
            if (this->client.call(srv)) {
                this->setOutput("key", srv.response.key);
                return BT::NodeStatus::SUCCESS;
            }
            else {
                return BT::NodeStatus::FAILURE;
            }
        }
};