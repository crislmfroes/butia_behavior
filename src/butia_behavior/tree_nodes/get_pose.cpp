#include "behaviortree_cpp_v3/behavior_tree.h"
#include "ros/ros.h"
#include "geometry_msgs/Point.h"
#include "geometry_msgs/Pose.h"
#include "butia_world_msgs/GetPose.h"
#include "stdlib.h"
#include "math.h"

class GetPoseAction : public BT::CoroActionNode
{
private:
    std::string service;
    ros::ServiceClient client;
    ros::NodeHandle n;

    double euclidDist(geometry_msgs::Point p1, geometry_msgs::Point p2) {
        return sqrt(pow(p1.x - p2.x, 2)+pow(p1.y - p2.y, 2));
    }

public:
    GetPoseAction(const std::string &name, const BT::NodeConfiguration &config) : BT::CoroActionNode(name, config)
    {
    }

    static BT::PortsList providedPorts()
    {
        return {
            BT::InputPort<std::string>("service"),
            BT::InputPort<std::string>("key"),
            BT::OutputPort<geometry_msgs::Pose>("pose")};
    }

    BT::NodeStatus tick() override
    {
        auto serviceOptional = this->getInput<std::string>("service");
        auto keyOptional = this->getInput<std::string>("key");
        this->service = serviceOptional.value_or("/butia_world/get_pose");
        if (!keyOptional)
        {
            throw BT::RuntimeError("missing required input [key]: ", keyOptional.error());
        }
        this->client = n.serviceClient<butia_world_msgs::GetPose>(this->service);
        this->client.waitForExistence();
        butia_world_msgs::GetPose srvKey;
        srvKey.request.key = keyOptional.value() + "/pose";
        butia_world_msgs::GetPose srvExit;
        srvExit.request.key = "exit";
        if (this->client.call(srvExit) && this->client.call(srvKey))
        {
            if (this->euclidDist(srvKey.response.pose.position, srvExit.response.pose.position)) {
                return BT::NodeStatus::SUCCESS;
            }
            this->setOutput("pose", srvKey.response.pose);
            this->setStatusRunningAndYield();
        }
        else
        {
            return BT::NodeStatus::FAILURE;
        }
    }
};