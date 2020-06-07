#include "behaviortree_cpp_v3/behavior_tree.h"
#include "string"
#include "list"
#include "map"
#include "utility"

class PrepareSpeechAction : public BT::SyncActionNode
{

public:
    PrepareSpeechAction(const std::string &name, const BT::NodeConfiguration &config) : BT::SyncActionNode(name, config)
    {
    }

    static BT::PortsList providedPorts()
    {
        return {
            BT::InputPort<std::string>("prefix"),
            BT::InputPort<std::string>("string_format"),
            BT::InputPort<std::string>("sufix"),
            BT::InputPort<std::map<std::string, int>>("registers"),
            BT::OutputPort<std::string>("text"),
        };
    }

    BT::NodeStatus tick() override
    {
        auto prefixOptional = this->getInput<std::string>("prefix");
        if (!prefixOptional)
        {
            throw BT::RuntimeError("missing required input [prefix]: ", prefixOptional.error());
        }
        auto stringFormatOptional = this->getInput<std::string>("string_format");
        if (!stringFormatOptional)
        {
            throw BT::RuntimeError("missing required input [string_format]: ", stringFormatOptional.error());
        }
        auto sufixOptional = this->getInput<std::string>("sufix");
        if (!sufixOptional)
        {
            throw BT::RuntimeError("missing required input [sufix]: ", sufixOptional.error());
        }
        auto registersOptional = this->getInput<std::map<std::string, int>>("registers");
        if (!registersOptional)
        {
            throw BT::RuntimeError("missing required input [registers]: ", registersOptional.error());
        }
        std::string text = prefixOptional.value() + "";
        std::list<std::string> micro_sentences;
        for (auto &&pair : registersOptional.value())
        {
            std::string microSentence = stringFormatOptional.value();
            std::string x;
            std::string key;
            pair.first.copy(key);
            for (auto &&tkn : std::strtok(key, "/"))
            {
                
            }
            
            std::snprintf(microSentence.data(), 10, stringFormatOptional.value().data(), )
        }
        
    }
};