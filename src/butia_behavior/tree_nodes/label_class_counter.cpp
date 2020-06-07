#include "behaviortree_cpp_v3/behavior_tree.h"
#include "ros/ros.h"
#include "butia_vision_msgs/Recognitions.h"
#include "stdlib.h"

class ClassCountHistoryAction : public BT::CoroActionNode
{
private:
    std::string topic;
    ros::Subscriber sub;
    ros::NodeHandle n;
    std::map<std::string, std::list<int>> countsHistory;
    int frameCounter;
    int windowSize;

    void onRecognitions(const butia_vision_msgs::Recognitions::ConstPtr msg)
    {
        std::map<std::string, int> frameCounts;
        for (auto &&description : msg->descriptions)
        {
            frameCounts[description.label_class] += 1;
        }
        for (auto &&pair : frameCounts)
        {
            this->countsHistory[pair.first].push_back(pair.second);
        }
        this->frameCounter += 1;
        if (this->frameCounter >= this->windowSize)
        {
            this->setOutput("counts_history", this->countsHistory);
            this->setStatus(BT::NodeStatus::SUCCESS);
        }
    }

public:
    ClassCountHistoryAction(const std::string &name, const BT::NodeConfiguration &config) : BT::CoroActionNode(name, config)
    {
    }

    static BT::PortsList providedPorts()
    {
        return {
            BT::InputPort<std::string>("topic"),
            BT::InputPort<int>("window_size"),
            BT::OutputPort<std::map<std::string, std::list<int>>>("counts_history")};
    }

    BT::NodeStatus tick() override
    {
        auto topicOptional = this->getInput<std::string>("topic");
        auto windowSizeOptional = this->getInput<int>("window_size");
        if (!topicOptional)
        {
            throw BT::RuntimeError("missing required input [topic]: ", topicOptional.error());
        }
        if (!windowSizeOptional)
        {
            throw BT::RuntimeError("missing required input [window_size]: ", windowSizeOptional.error());
        }
        this->windowSize = windowSizeOptional.value();
        this->topic = topicOptional.value();
        this->sub = this->n.subscribe(this->topic, 1000, ClassCountHistoryAction::onRecognitions, this);
        this->setStatusRunningAndYield();
    }
};