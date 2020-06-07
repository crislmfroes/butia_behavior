#include "behaviortree_cpp_v3/behavior_tree.h"
#include "ros/ros.h"
#include "actionlib/client/simple_action_client.h"
#include "geometry_msgs/Point.h"
#include "geometry_msgs/Pose.h"
#include "move_base_msgs/MoveBaseAction.h"
#include "move_base_msgs/MoveBaseGoal.h"
#include "stdlib.h"
#include "math.h"

typedef actionlib::SimpleActionClient<move_base_msgs::MoveBaseAction> Client;

class GoToAction : public BT::CoroActionNode
{
private:
    Client client = Client("move_base", false);

public:
    GoToAction(const std::string &name, const BT::NodeConfiguration &config) : BT::CoroActionNode(name, config)
    {
    }

    static BT::PortsList providedPorts()
    {
        return {
            BT::InputPort<std::string>("frame"),
            BT::InputPort<geometry_msgs::Pose>("pose")
        };
    }

    BT::NodeStatus tick() override
    {
        std::string frame = this->getInput<std::string>("frame").value_or("map");
        auto poseOptional = this->getInput<geometry_msgs::Pose>("pose");
        if (!poseOptional) {
            throw BT::RuntimeError("missing required input [pose]: ", poseOptional.error());
        }
        this->client.waitForServer();
        move_base_msgs::MoveBaseGoal goal;
        goal.target_pose.header.frame_id = frame;
        goal.target_pose.header.stamp = ros::Time::now();
        goal.target_pose.pose = poseOptional.value();
        this->client.sendGoal(goal);
        this->setStatusRunningAndYield();
        if (this->client.waitForResult()) {
            return BT::NodeStatus::SUCCESS;
        } else {
            return BT::NodeStatus::FAILURE;
        }
    }
};